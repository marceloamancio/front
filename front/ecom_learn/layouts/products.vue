<template>
    <div>
    l2
    <header>
        <NuxtLink to="/products">Nuxt Dojo Merch</NuxtLink>
        <nav>
            <ul>
                <li><NuxtLink to="/products/product"> Product inside </NuxtLink>  </li>
                <li><NuxtLink to="/products/23"> Product 23 </NuxtLink>  </li>
            </ul>
        </nav>
    </header>

    <!-- output the page content -->
    <div>
        <slot />
    </div>

    <footer>
        <nav>
            <ul>
                <NuxtLink to="/">Nuxt Dojo</NuxtLink>
                <li><NuxtLink to="/"> Home </NuxtLink>  </li>
                <li><NuxtLink to="/products"> Products </NuxtLink>  </li>
                <li><NuxtLink to="/about"> About </NuxtLink>  </li>
            </ul>
        </nav>
    </footer>
    </div>
</template>

<style>
    .router-link-exact-active {
        color: #12b488;
    }
</style>