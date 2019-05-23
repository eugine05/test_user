<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">
            Пользователи
        </mu-appbar>
        <mu-row>
            <h1></h1>
        </mu-row>

        <slot></slot>
    </mu-container>
</template>

<script>

    export default {
        name: "Home",
    }
</script>

<style scoped>

</style>
