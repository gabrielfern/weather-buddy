<script>
    export let city
    export let spotlight
</script>

<div class:shadow={spotlight}>
    <p>{city.name}</p>
    <p class='temperature'>{city.temperature} °C</p>
    <p>{city.weather}</p>
</div>

<style>
    div {
        padding: 10px;
        margin: 10px;
        width: 150px;
        text-align: center;
        border: 1px solid black;
    }

    .temperature {
        font-size: xx-large;
    }

    .shadow {
        box-shadow: 5px 5px;
    }
</style>
