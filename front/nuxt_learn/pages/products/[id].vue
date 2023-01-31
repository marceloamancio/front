<template>
    <div>
        <p>Product details for {{  id  }}</p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim nobis eos amet voluptatibus odio vel incidunt commodi temporibus minima. Iste!</p>
    </div>
</template>

<script setup>
   const { id } = useRoute().params
   
   definePageMeta({
        layout: 'products'
    })
</script>

<style scoped>

</style>