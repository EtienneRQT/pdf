from app.chat.tracing.langfuse import langfuse


class TraceableChain:
    def __call__(self, *args, **kwargs):
        trace = langfuse.trace(
            id=self.metadata["conversation_id"],  # type: ignore
            metadata=self.metadata,  # type: ignore
        )

        callbacks = kwargs.get("callbacks", []) or []
        callbacks.append(trace.getNewHandler())  # type: ignore
        kwargs["callbacks"] = callbacks
        return super().__call__(*args, **kwargs)  # type: ignore
