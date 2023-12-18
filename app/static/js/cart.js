function addToCart(id, name, price) {
    fetch('/api/cart',{
        method: 'post',
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            'Content-Type': "application/json"
        }
    }
    )
    .then(function(res) {
        return res.json()
    })
    .then(function(data) {
        document.querySelector('.cart-counter').innerText = data.total_quantity
        console.log(data)
    })
}