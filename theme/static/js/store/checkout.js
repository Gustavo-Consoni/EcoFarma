document.addEventListener('alpine:init', () => {
    Alpine.data('checkout', (csrf_token, STRIPE_PUBLIC_KEY) => ({

        loading: false,
        stripe: Stripe(STRIPE_PUBLIC_KEY),
        csrf_token: csrf_token,

        create_checkout_session() {
            fetch('api/v1/create_checkout_session', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.csrf_token,
                },
                body: JSON.stringify({
                    products: JSON.parse(localStorage.getItem('cart')),
                })
            })
            .then(response => response.json())
            .then(session => {
                return this.stripe.redirectToCheckout({ sessionId: session.id })
            })
            .then(result => {
                if (result.error) {
                    alert(result.error.message)
                }
            })
            .catch(error => {
                console.error('Error:', error)
            })
        }

    }))
});
