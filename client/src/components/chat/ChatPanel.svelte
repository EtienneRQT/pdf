<script lang="ts">
	import { onMount } from 'svelte';
	import {
		store,
		resetError,
		fetchConversations,
		createConversation,
		getActiveConversation
	} from '$s/chat';
	import Alert from '$c/Alert.svelte';
	import ChatInput from '$c/chat/ChatInput.svelte';
	import ChatList from '$c/chat/ChatList.svelte';
	import ConversationSelect from '$c/chat/ConversationSelect.svelte';

	export let onSubmit: (text: string, useStreaming: boolean) => void;
	export let documentId: number;

	let useStreaming = !!localStorage.getItem('streaming');

	$: localStorage.setItem('streaming', useStreaming ? 'true' : '');
	$: activeConversation = $store.activeConversationId ? getActiveConversation() : null;

	function handleSubmit(event: CustomEvent<string>) {
		if (onSubmit) {
			onSubmit(event.detail, useStreaming);
		}
	}

	function handleNewChat() {
		createConversation(documentId);
	}

	onMount(() => {
		fetchConversations(documentId);
	});
</script>

<div
    style="height: calc(100vh - 80px);"
    class="flex flex-col h-full bg-slate-100 border-2 border-slate-200 rounded-2xl shadow-lg overflow-hidden"
>
    <div class="bg-slate-200 rounded-t-2xl px-4 py-3 flex flex-row items-center justify-between shadow-sm">
        <div class="opacity-70 flex items-center gap-2">
            <input id="chat-type" type="checkbox" bind:checked={useStreaming} class="rounded text-blue-500 focus:ring-blue-500 focus:border-blue-500" />
            <label for="chat-type" class="italic text-sm">Streaming</label>
        </div>
        <div class="flex gap-3 items-center">
            <ConversationSelect conversations={$store.conversations} />
            <button class="rounded-lg text-sm border border-blue-500 bg-blue-500 text-white px-3 py-1.5 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition duration-300 ease-in-out"
                on:click={handleNewChat}>New Chat</button>
        </div>
    </div>
    <div class="flex flex-col flex-1 px-4 py-3 overflow-y-auto">
        <ChatList messages={activeConversation?.messages || []} />
        <div class="relative mt-4">
            {#if $store.error && $store.error.length < 200}
                <div class="p-4">
                    <Alert type="error" onDismiss={resetError}>
                        {$store.error}
                    </Alert>
                </div>
            {/if}
            <ChatInput on:submit={handleSubmit} />
        </div>
    </div>
</div>
