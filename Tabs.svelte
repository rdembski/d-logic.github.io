<script>
    import { onMount } from 'svelte';
    let isTabVisible = false;

    onMount(() => {
        isTabVisible = true;
    });

    function selectTab() {
        if (isTabVisible) {
            // Kod do wyboru zakładki
            console.log("Tab selected");
        }
    }
</script>

<button on:click={selectTab}>Wybierz zakładkę</button>
