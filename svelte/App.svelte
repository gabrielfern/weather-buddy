<script>
    import City from './City.svelte'
    import { onMount, afterUpdate } from 'svelte'

    let cities = []
    let city_name = ''
    let input_disabled = false
    let error_msg = ''
    let city
    let input

    async function load_cities() {
        let resp = await fetch('API_BASE_URL/api/weather')
        cities = await resp.json()
    }

    async function retrieve_city() {
        input_disabled = true
        error_msg = ''

        try {
            let resp = await fetch(`API_BASE_URL/api/weather/${city_name}`)
            if (resp.status == 200) {
                city = await resp.json()
                city_name = ''
                load_cities()
            } else if (resp.status == 404) {
                error_msg = 'Sorry. We couldn\'t find the specified city.'
            } else {
                throw Error()
            }
        } catch {
            error_msg = 'An error has occurred.'
        }

        input_disabled = false
    }

    onMount(load_cities)
    afterUpdate(() => input && input.focus())
</script>

<div class='container'>
    <h1>Weather Buddy</h1>

    <form on:submit|preventDefault={retrieve_city}>
        How is the weather in
        <input bind:value={city_name} type='text' disabled={input_disabled} bind:this={input}>
        now?
    </form>

    {#if error_msg}
        <h3 class='error'>{error_msg}</h3>
    {/if}

    {#if city}
        <div class='inner-container'>
            <City city={city} spotlight={true} />
        </div>
    {/if}

    <div class='inner-container'>
        {#each cities as city}
            <City city={city} spotlight={false} />
        {/each}
    </div>
</div>

<style>
    h1, form {
        margin-bottom: 30px;
    }

    input {
        border-top: none;
        border-left: none;
        border-right: none;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .inner-container {
        margin-top: 50px;
        margin-bottom: 50px;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }

    .error {
        color: red;
    }
</style>
