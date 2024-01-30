document.addEventListener('alpine:init', () => {
    Alpine.data('home', () => ({

        products: [],

        init() {
            this.get_products()
        },

        get_products() {
            fetch('/api/v1/products', {
                method: 'GET',
            })  
            .then(response => response.json())
            .then((data) => {
                this.products = data
            })
        },

    }))
})
