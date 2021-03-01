<script>
    let cities = []
    async function load_cities() {
        let resp = await fetch('API_BASE_URL/api/weather')
        cities = await resp.json()
    }
    load_cities()

    let city_name = ''
    let input_disabled = false
    async function retrieve_city() {
        input_disabled = true
        await fetch(`API_BASE_URL/api/weather/${city_name}`)
        await load_cities()
        city_name = ''
        input_disabled = false
    }
</script>

<div class='container'>
    <h1>Weather Buddy</h1>

    <form on:submit|preventDefault={retrieve_city}>
        <input bind:value={city_name} type='text' disabled={input_disabled}>
        <button type='submit' disabled={input_disabled}>Go</button>
    </form>

    {#each cities as city}
        <h4>{city.name} ({city.temperature} °C)</h4>
    {/each}
</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
