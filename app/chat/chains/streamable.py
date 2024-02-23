from flask import current_app
from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler


class StreamableChain:

    def stream(self, input):
        """Stream input through the agent and return a generator
        that yields tokens from the streaming callbacks.

        Spawns a background thread to run the agent and collect
        tokens from the streaming callback handlers. Safe to call
        multiple times and from multiple threads."""
        queue = Queue()
        handler = StreamingHandler(queue)

        def task(app_context):
            app_context.push()
            self(input, callbacks=[handler])  # type: ignore

        Thread(target=task, args=[current_app.app_context()]).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token
