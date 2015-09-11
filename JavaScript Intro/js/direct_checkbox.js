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
    this.checked = false;
    this.adjustStock = function (num) {
        return this.stock -= num;
    };
    this.inStock = function() {
        return this.stock > 0;
    };
}

function checkAll(checkbox) {
    // find all checbox inputs on page
    var inputs = inventory.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {

        if (inputs[i].type === 'checkbox') {
            if (checkbox.checked) {
                inputs[i].checked = true;
                products[i].checked = true;
            }
            else {
                inputs[i].checked = false;
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

    if (isNaN(parseInt(price)) || isNaN(parseFloat(price))) {
        errorMessage.innerHTML = "You must enter a 'digit' for the price";
    } else if (material.length > 0 && price.length > 0) {
        products.push(new Product(material, 10, price));
        populateInventory();

    } else {
        errorMessage.innerHTML = "Your material must be greater than 3 chars, and your price must be greater than 1";
    }
    // clear form inputs.
    document.getElementById('material').value = "";

    document.getElementById('price').value = "";
}

function populateInventoryBad() {
    var fullInventory = "";

    for (var i = 0; i < products.length; i++) {
        console.log(products[i]);
        var newRow = "<tr><td><input type='checkbox'/></td><td>" +
            products[i].name +
            "</td><td>$" + products[i].price + "</td>" +
            "<td class=" + products[i].inStock() + ">" +
            (products[i].inStock() ? "Yes" : "No") + "</td></tr>";
        if (products[i].checked) {
        }
        fullInventory += newRow;
    }
    inventory.innerHTML = fullInventory;

    var inputs = inventory.getElementsByTagName('input');
    for (var j = 0; j < inputs.length; j++) {
        if (inputs[i].type === 'checkbox') {
            if (products[i].checked) {
                inputs[i].checked = true;
            }
        }
    }
}

function populateInventory(){

    for (var i=0; i < products.length; i++) {
        var newProdRow = document.createElement('tr');
        var checkboxCell = document.createElement('td');
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = products[i].checked;
        checkboxCell.appendChild(checkbox);
        newProdRow.appendChild(checkboxCell);

        // Name Column
        var nameCol = document.createElement('td');
        var nameText = document.createTextNode(products[i].name);
        nameCol.appendChild(nameText);
        newProdRow.appendChild(nameCol);

        // Price Column
        var priceCol = document.createElement('td');
        var priceText = document.createTextNode('$' + products[i].price);
        priceCol.appendChild(priceText);
        newProdRow.appendChild(priceCol);

        // Stock Column
        var stockCol = document.createElement('td');
        stockCol.className = products[i].inStock();
        var stockText = document.createElement(products[i].stock);
        stockCol.appendChild(stockText);
        newProdRow.appendChild(stockCol);

        inventory.appendChild(newProdRow);
    }

}

// Init Material & Add initialized row.
products.push(new Product('wood', 10, 15));
populateInventory();
