function load_prod(get_all_product) {
    $.ajax({
        url: ' ',
        type: 'GET',
        data: JSON.stringify({product}),
        contentType: "application/json; charset=utf-8",
        success: function (response) {
            var r = confirm("get product " + all_product + " success !!!");
            if (r === true) {window.location.reload();}
        }
    });
}