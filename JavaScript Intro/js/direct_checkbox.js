/**
 * Created by Maxwell J. Resnick on 8/26/15.
 */
var inventory = document.getElementById('inventory');
var material, price;
var errorMessage = document.getElementById('error');
var products = [];
function Product(name, stock, price) {
    this.name = name;
    this.stock = stock;
    this.price = price;

    this.adjustStock = function (num) {
        return this.stock -= num
    };

    this.inStock = function() {
        return this.stock > 0;
    };
}

products.push(new Product('wood', 10, 15));
console.log(products);
function checkAll(checkbox) {
    // find all checbox inputs on page
    var inputs = inventory.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        console.log(inputs);
        if (inputs[i].type === 'checkbox') {
            if (checkbox.checked) {
                inputs[i].setAttribute('checked', '');
            }
            else {
                inputs[i].removeAttribute('checked');
            }

        }
    }

}
function removeStock() {
    var rows = inventory.getElementsByTagName('tr');
    for (var i= 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type === 'checkbox') {
            if (inputs[0].checked) {
                var stock = rows[i].lastElementChild;
                stock.className = 'false';
                stock.textContent = 'No';
                inputs[0].checked = false;
            }
        }
    }

}

function addStock() {
    var rows = inventory.getElementsByTagName('tr');
    for (var i=0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type === 'checkbox') {
            if (inputs[0].checked) {
                var stock = rows[i].lastElementChild;
                stock.className = 'true';
                stock.textContent = 'Yes';
                inputs[0].checked = false;
            }
        }
    }
}

function addNewStock() {
    material = document.getElementById('material').value;
    price = document.getElementById('price').value;
    errorMessage.innerHTML = "";

    if (isNaN(parseInt(price))) {
         errorMessage.innerHTML = "You must enter a 'digit' for the price";
    } else if (material.length > 0 && price.length > 0) {
        var newRow = "<tr><td><input type='checkbox'/></td><td>" +
                material +
                "</td><td>$" + price + "</td>" +
                "<td class='false'>No</td></tr>";
        inventory.innerHTML += newRow;
    } else {
        errorMessage.innerHTML = "Your material must be greater than 3 chars, and your price must be greater than 1";
    }

    // clear form inputs.
    document.getElementById('material').value = "";
    document.getElementById('price').value = "";
}