<script lang="ts">
    import AssistantMessage from '$c/chat/AssistantMessage.svelte';
    import UserMessage from '$c/chat/UserMessage.svelte';
    import PendingMessage from '$c/chat/PendingMessage.svelte';

    interface Message {
        role: 'user' | 'system' | 'assistant' | 'pending' | 'human' | 'ai';
        content: string;
    }
    export let messages: Message[] = [];

    const scrollIntoView = (node: HTMLDivElement, _m: any) => {
        setTimeout(() => {
            node.scrollIntoView({ behavior: 'smooth' });
        }, 0);
        return {
            update: () => node.scrollIntoView({ behavior: 'smooth' })
        };
    };
</script>

<div class="flex flex-col flex-1 overflow-y-auto bg-gray-100 rounded-lg shadow px-3 py-4">
    <div class="flex flex-col gap-3">
        {#each messages as message}
            {#if message.role === 'user' || message.role === 'human'}
                <UserMessage content={message.content} />
            {:else if message.role === 'assistant' || message.role === 'ai'}
                <AssistantMessage content={message.content} />
            {:else if message.role === 'pending'}
                <PendingMessage />
            {/if}
        {/each}
    </div>
    <div class="pt-4" use:scrollIntoView={messages} />
</div>
