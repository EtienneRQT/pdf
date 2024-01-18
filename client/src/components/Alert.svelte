<script lang="ts">
    import classNames from 'classnames';

    export let onDismiss: (() => void) | null = null;
    export let type: 'error' | 'success' | 'info' | 'warning' = 'error';

    const klasses = {
        error: 'bg-red-100 border border-red-300 text-sm text-red-800 rounded-lg p-4 shadow',
        success: 'bg-green-100 border border-green-300 text-sm text-green-800 rounded-lg p-4 shadow',
        info: 'bg-blue-100 border border-blue-300 text-sm text-blue-800 rounded-lg p-4 shadow',
        warning: 'bg-yellow-100 border border-yellow-300 text-sm text-yellow-800 rounded-lg p-4 shadow'
    };
    const klass = classNames(klasses[type], 'relative flex justify-between items-center');

    function handleDismiss() {
        if (onDismiss) {
            onDismiss();
        }
    }
</script>

<div class={klass} role="alert">
    <slot />

    {#if onDismiss}
        <button
            on:click={handleDismiss}
            class="text-lg font-semibold text-gray-600 hover:text-gray-800 transition duration-300 ease-in-out"
            aria-label="Close"
        >
            ×
        </button>
    {/if}
</div>
