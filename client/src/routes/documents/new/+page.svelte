<script lang="ts">
	import { goto, beforeNavigate } from '$app/navigation';
	import Alert from '$c/Alert.svelte';
	import Button from '$c/Button.svelte';
	import { documents, upload, clearErrors } from '$s/documents';
	import Progress from '$c/Progress.svelte';

	let files: FileList;
	let loading = false;
	let uploadComplete = false;

	async function handleSubmit() {
		loading = true;
		await upload(files[0]);
		if (!$documents.error) {
			uploadComplete = true;

			setTimeout(() => {
				goto('/documents');
				loading = false;
			}, 2000);
		} else {
			loading = false;
		}
	}

	beforeNavigate(clearErrors);
</script>

<div class="w-full max-w-md mx-auto p-6 bg-white rounded-lg shadow-lg">
    <h2 class="text-3xl font-bold mb-10 text-center">Upload a Document</h2>
    <form on:submit|preventDefault={handleSubmit}>
        <div class="w-42 mb-6">
            <label for="file-input" class="block mb-2 text-sm font-medium text-gray-700">Choose file</label>
            <input
                bind:files
                type="file"
                name="file-input"
                id="file-input"
                class="block w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 cursor-pointer focus:border-blue-500 focus:ring-blue-500 file:mr-4 file:py-2 file:px-4 file:m-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-violet-700 hover:file:bg-violet-100 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
            />
        </div>

        {#if loading && !$documents.error}
            <Progress progress={$documents.uploadProgress}>
                <Alert type="success">Upload Complete! Returning to list...</Alert>
            </Progress>
        {/if}

        {#if $documents.error}
            <Alert type="error">Error: {$documents.error}</Alert>
        {/if}

        {#if !loading}
            <Button className="w-full mt-4 mb-3" disabled={loading}>Submit</Button>
        {/if}
    </form>
</div>

