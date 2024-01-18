<script lang="ts">
    import { marked } from 'marked';

    export let content = '';
</script>

<div class="message border-2 border-slate-300 rounded-lg shadow-sm py-2 px-3 my-1 break-words self-end bg-slate-100 text-gray-800">
    {@html marked(content, { breaks: true, gfm: true })}
</div>

<style>
    .message {
        max-width: 80%;
        word-wrap: break-word;
    }
</style>
