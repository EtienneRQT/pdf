<script lang="ts">
    import { marked } from 'marked';
    import classnames from 'classnames';
    import { scoreConversation } from '$s/chat';
    import Icon from '$c/Icon.svelte';

    export let content = '';
    let score = 0;

    const baseKlass = 'border rounded-full inline-block cursor-pointer transition-colors duration-300 ease-in-out';
    $: upKlass = classnames(baseKlass, {
        'hover:bg-green-200 bg-green-100': score === 1,
        'hover:bg-gray-200': score !== 1,
    });
    $: downKlass = classnames(baseKlass, {
        'hover:bg-red-200 bg-red-100': score === -1,
        'hover:bg-gray-200': score !== -1,
    });

    async function applyScore(_score: number) {
        if (score !== 0) {
            return;
        }
        score = _score;
        return scoreConversation(_score);
    }
</script>

<div class="flex flex-row items-center justify-between">
    <div
        class="message border rounded-md py-2 px-3 my-1 break-words self-start bg-blue-600 text-white shadow"
    >
        {@html marked(content, { breaks: true, gfm: true })}
    </div>
    <div class="flex flex-row flex-1 items-start gap-2 flex-wrap justify-center">
        {#if score >= 0}
            <div class={upKlass} style="line-height: 12px; padding: 8px;">
                <Icon on:click={() => applyScore(1)} name="thumb_up" outlined />
            </div>
        {/if}
        {#if score <= 0}
            <div class={downKlass} style="line-height: 12px; padding: 8px;">
                <Icon on:click={() => applyScore(-1)} name="thumb_down" outlined />
            </div>
        {/if}
    </div>
</div>

<style>
    .message {
        max-width: 80%;
        word-wrap: break-word;
    }
</style>
