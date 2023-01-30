<template>
    <div>
    <header>
    l1
        <nav>
            <ul>
                <NuxtLink to="/">Nuxt Dojo</NuxtLink>
                <li><NuxtLink to="/"> Home </NuxtLink>  </li>
                <li><NuxtLink to="/products"> Products </NuxtLink>  </li>
                <li><NuxtLink to="/about"> About </NuxtLink>  </li>
            </ul>
        </nav>
    </header>

    <!-- output the page content -->
    <div>
        <slot />
    </div>
    </div>
</template>

<style>
    .router-link-exact-active {
        color: #12b488;
    }
</style>