$(document).ready(function() {
    jQuery.support.cors = true;
    get_page(0);
});

function get_page(current_page) {
    get_products(current_page);
    gen_pagging(current_page);
}

function gen_pagging(current_page) {
    $.ajax({
        url: 'http://localhost:6868/food-blog/api/product?count=1',
        crossDomain : true,
        dataType : "jsonp",
        type: 'GET',
        jsonp: "callback",
        contentType: "application/json; charset=utf-8",
        success: function(data, state, res){
            if (data == null) { return; };
            $('#pagging').empty().append(reder_page(data['count'], current_page));
            $('#count_tag').empty().append("Show result " + String(data['count']));
        }
    });
}

function reder_page(product_count, current_page) {
    var page_count = Math.ceil(product_count / 9);
    var htmlText = '<li><span>Pages</span></li>';

    for (var i = 0; i < page_count; i++) {
        if (current_page == i) {
            htmlText += '<li class="active"><a href="#" onclick="get_page(' + i + ')">' + String(i + 1) + '</a></li>';
        } else {
            htmlText += '<li><a href="#" onclick="get_page(' + i + ')">' + String(i + 1) + '</a></li>';
        }
    }
    var previous_page = Math.max(current_page - 1, 0);
    var nex_page = Math.min(current_page + 1, page_count - 1);

    htmlText += '<li class="float-right">';
    htmlText += '<a aria-label="Previous" onclick="get_page(' + previous_page + ')"><i class="arrow_left"></i></a>';
    htmlText += '<a aria-label="Next" onclick="get_page(' + nex_page + ')"><i class="arrow_right"></i></a>';
    htmlText += '</li>';
    return htmlText;
}

function get_products(page) {
    $.ajax({
        url: 'http://localhost:6868/food-blog/api/product?size=9&page=' + page,
        crossDomain : true,
        dataType : "jsonp",
        type: 'GET',
        jsonp: "callback",
        contentType: "application/json; charset=utf-8",
        success: function(data, state, res){
            if (data == null) { return; };
            var items = [];
            $.each(data, function(index, item) {
                items.push(reder_products(item));
            });
            $('#products').empty().append(items.join(""));
        }
    });
}


function reder_products(item) {
    var htmlText = '<div class="product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12">';
    htmlText += '<div class="product-thumb">';
    htmlText += '<div class="image">';
    htmlText += '<a class="rec-fill front front--slide-left" href="shopdetail.html"><img src="http://localhost:6868/static/' + item['BigImage1'] + '" alt="image" title="image" class="img-fluid" /></a>';
    htmlText += '<a class="rec-fill back back--slide-left" href="shopdetail.html"><img src="http://localhost:6868/static/' + item['BigImage2'] + '" alt="image" title="image" class="img-fluid" /></a>';
    if (item['BestSell'] == 1) {
        htmlText += '<div class="sale"><p>Sale</p></div>';
    }
    htmlText += '<div class="onhover">';
    htmlText += '<ul class="list-inline">';
    htmlText += '<ul class="list-inline">';
    htmlText += '<li><a href="#"><i class="fa fa-shopping-cart"></i> Add to cart</a></li>';
    htmlText += '<li><a href="#"><i class="fa fa-heart"></i></a></li>';
    htmlText += '<li><a href="#"><i class="fa fa-retweet"></i></a></li>';
    htmlText += '</ul>';
    htmlText += '</div>';
    htmlText += '</div>';
    htmlText += '<div class="caption">';
    htmlText += '<h4><a href="shopdetail.html?id=' + item['Id'] + '">' + item['Name'] + '</a></h4>';
    htmlText += (item['OldPrice']) && (item['OldPrice'] > 0) ? '<p class="price"><span class="price-old">$' + item['OldPrice'] + "</span> $" : "<p class='price'> $";
    htmlText += item['Price']  + "</p>";
    htmlText += '<div class="rating">';
    for (var i = 0; i < 5; i++) {
        htmlText += ((i + 1) == item['Vote']) ? "<i class='fa fa-star-o'></i>" : "<i class='fa fa-star'></i>";
    }
    htmlText += '</div>';
    htmlText += '<p class="des">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas non eleifend erat, vitae aliquam metus. Donec orci tellus, rhoncus eget ipsum tempus, dignissim rutrum enim. Integer interdum sapien nec tempus luctus.</p';
    htmlText += '<div class="button-group">';
    htmlText += '<button type="button"><i class="fa fa-shopping-cart"></i></button>';
    htmlText += '<button type="button"><i class="fa fa-heart"></i></button>';
    htmlText += '<button type="button"><i class="fa fa-retweet"></i></button>';
    htmlText += '</div>';
    htmlText += '</div>';
    htmlText += '</div>';
    htmlText += '</div>';
    htmlText += '</div>';
    return htmlText;
}