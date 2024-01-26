<script lang="ts">
    import { createEventDispatcher } from 'svelte';

    let value = '';

    const dispatch = createEventDispatcher();
    function handleKeyDown(event: KeyboardEvent) {
        const isCombo = event.shiftKey || event.ctrlKey || event.altKey || event.metaKey;
        if (event.key !== 'Enter' || isCombo) {
            return;
        }

        if (event.key === 'Enter' && !isCombo && value === '') {
            event.preventDefault();
            return;
        }

        event.preventDefault();
        dispatch('submit', value);
        value = '';
    }

    $: height = (value.match(/\n/g)?.length || 0) * 25 + 72;
</script>

<textarea
    class="w-full mx-auto py-2 px-3 resize-none border-2 border-gray-300 rounded-lg max-h-40 shadow-sm focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500 transition-all duration-300 ease-in-out"
    style:height={height + 'px'}
    bind:value
    on:keydown={handleKeyDown}
    placeholder="Type your message..."
/>
