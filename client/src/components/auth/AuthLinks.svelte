<script lang="ts">
    import { auth } from '$s/auth';
</script>

{#if $auth.user}
    <a
        class="font-semibold text-white hover:text-indigo-300 transition-colors duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 rounded-lg px-3 py-1"
        href="/auth/signout">Sign Out</a
    >
{:else}
    <a
        class="font-semibold text-white hover:text-indigo-300 transition-colors duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 rounded-lg px-3 py-1 mx-2"
        href="/auth/signin">Login</a
    >
    <a
        class="font-semibold text-white hover:text-indigo-300 transition-colors duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 rounded-lg px-3 py-1"
        href="/auth/signup">Sign Up</a
    >
{/if}
