document.addEventListener('alpine:init', () => {
    Alpine.data('cart', () => ({

        product: '',
        cart: localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : [],
        cartModal: false,
        sidebarModal: false,

        toggleModals() {
            if (this.cartModal) {
                this.cartModal = !this.cartModal
            } else if (this.sidebarModal) {
                this.sidebarModal = !this.sidebarModal
            }
        },

        addToCart(product) {
            !localStorage.getItem('cart') ? localStorage.setItem('cart', JSON.stringify([])) : undefined
            cart = JSON.parse(localStorage.getItem('cart'))
            productIndex = cart.findIndex(item => item.id == product.id)
            if (productIndex == -1) {
                product['volume'] = 1
                this.cart.push(product)
            } else {
                this.cart.find(item => item.id === product.id)['volume'] += 1
            }
            this.cartModal = true
            localStorage.setItem('cart', JSON.stringify(this.cart))
        },

        removeToCart(product) {
            cart = JSON.parse(localStorage.getItem('cart'))
            productIndex = cart.findIndex(item => item.id == product.id)
            if (productIndex !== -1) {
                this.cart.splice(this.cart.findIndex(item => item.id == product.id), 1)
                localStorage.setItem('cart', JSON.stringify(this.cart))
            }
        },

        increaseAmount(product) {
            cart = JSON.parse(localStorage.getItem('cart'))
            productIndex = cart.findIndex(item => item.id == product.id)
            if (productIndex !== -1) {
                this.cart[cart.findIndex(item => item.id == product.id)].volume += 1
                localStorage.setItem('cart', JSON.stringify(this.cart))
            }
        },

        decreaseAmount(product) {
            cart = JSON.parse(localStorage.getItem('cart'))
            productIndex = cart.findIndex(item => item.id == product.id)
            if (productIndex !== -1) {
                if (product.volume <= 1) {
                    this.cart.splice(this.cart.findIndex(item => item.id == product.id), 1)
                } else {
                    this.cart[cart.findIndex(item => item.id == product.id)].volume -= 1
                }
                localStorage.setItem('cart', JSON.stringify(this.cart))
            }
        },

    }))
})
