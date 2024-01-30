document.addEventListener('alpine:init', () => {
    Alpine.data('product', () => ({

        products: [],
        product: '',

        init() {
            this.get_products()
            this.get_product()
        },

        get_products() {
            fetch('/api/v1/products?limit=5', {
                method: 'GET',
            })
            .then(response => response.json())
            .then((data) => {
                this.products = data
            })
        },

        get_product() {
            fetch('/api/v1/products/2', {
                method: 'GET',
            })
            .then(response => response.json())
            .then((data) => {
                this.product = data
            })
        },

    }))
})