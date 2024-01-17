<script lang="ts">
    import type { PageData } from './$types';
    import AuthGuard from '$c/AuthGuard.svelte';

    export let data: PageData;

    const documents = data.documents || [];
</script>

<AuthGuard />
<div class="flex flex-row justify-between items-center my-6">
    <h2 class="text-4xl font-extrabold text-gray-800 dark:text-white m-2">Your Documents</h2>
    <div>
        <a
            href="/documents/new"
            class="py-2 px-4 inline-flex justify-center items-center gap-2 rounded-md shadow-md font-bold bg-blue-600 text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all dark:focus:ring-offset-gray-800"
            >New</a
        >
    </div>
</div>

<div class="flex flex-col">
    <div class="overflow-x-auto shadow-lg rounded-lg">
        <div class="align-middle inline-block min-w-full">
            <div class="overflow-hidden rounded-lg">
                <table class="min-w-full divide-y divide-gray-300 dark:divide-gray-600">
                    <thead class="bg-gray-100 dark:bg-gray-800">
                        <tr>
                            <th
                                scope="col"
                                class="px-6 py-3 text-left text-sm font-semibold text-gray-700 dark:text-gray-300 uppercase">Name</th
                            >
                            <th
                                scope="col"
                                class="px-6 py-3 text-left text-sm font-semibold text-gray-700 dark:text-gray-300 uppercase">ID</th
                            >
                            <th
                                scope="col"
                                class="px-6 py-3 text-right text-sm font-semibold text-gray-700 dark:text-gray-300 uppercase">Action</th
                            >
                        </tr>
                    </thead>

                    <tbody class="bg-white divide-y divide-gray-200 dark:bg-gray-900 dark:divide-gray-700">
                        {#each documents as document}
                            <tr class="hover:bg-gray-100 dark:hover:bg-gray-800">
                                <td
                                    class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800 dark:text-gray-200"
                                    >{document.name}</td
                                >
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200"
                                    >{document.id}</td
                                >
                                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
    								<a class="text-blue-600 hover:text-white hover:bg-blue-800 rounded px-2 py-1 transition-colors duration-300" href="/documents/{document.id}">View</a>
								</td>

                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
