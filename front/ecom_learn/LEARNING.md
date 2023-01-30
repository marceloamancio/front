# Course [Nuxt 3 Tutorial - class 7](https://www.youtube.com/watch?v=dvanqBUoxhc&list=PL4cUxeGkcC9haQlqdCQyYmL_27TesCGPC&index=7)

# files
* nuxt.config.ts // main configuration file
* app.vue // project root file
* .nuxt // no need to change
* pages // .vue files under this directory will be automatically routed
* pages/index.vue  // will be the root '/' for the application
* products/index.vue // will make products be its own index products/ 
* vbase-3-setup extension command will generate:

```
<template>
    <div>

    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>

```

* Referint to product/[id].vue

```
<template>
    <div>
        <p>Product details for {{  id  }}</p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim nobis eos amet voluptatibus odio vel incidunt commodi temporibus minima. Iste!</p>
    </div>
</template>

<script setup>
   const { id } = useRoute().params 
</script>

<style scoped>

</style>
```

* Nuxt link component:

```
                <li><NuxtLink to="/"> Home </NuxtLink>  </li>
                <li><NuxtLink to="/products"> Products </NuxtLink>  </li>
```

* Define default template: layouts/default.vue