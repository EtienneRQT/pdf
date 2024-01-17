<script lang="ts">
    import AuthLinks from '$c/auth/AuthLinks.svelte';
    import { auth } from '$s/auth';

    $: user = $auth.user;
</script>

<header
    class="mb-4 bg-gradient-to-r from-indigo-600 to-purple-700 text-white shadow-lg py-4 z-50 w-full"
>
    <nav
        class="max-w-7xl w-full mx-auto px-6 sm:flex sm:items-center sm:justify-between"
        aria-label="Global"
    >
        <a class="flex-none text-2xl font-bold hover:text-indigo-300" href="/">Home</a>
        <div class="flex flex-row items-center gap-6 mt-5 sm:mt-0">
            {#if user}
                <a
                    class="font-semibold hover:text-indigo-300"
                    href="/scores">Scores</a
                >
                <a
                    class="font-semibold hover:text-indigo-300"
                    href="/documents">Documents</a
                >
            {/if}
            <AuthLinks />
        </div>
    </nav>
</header>
