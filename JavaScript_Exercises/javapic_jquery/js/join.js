/**
 * Created by Maxwell J. Resnick on 9/1/15.
 */
// Overkill for this assignment
var $jQ = jQuery.noConflict();

var form = {
    name: function (name) {
        this.isValid = /^([a-zA-Z]+)$/
            .test(name);
        this.errorMessage = "Your name must be chars only.";
        if (!this.isValid) {
            form.errors["name"] = this.errorMessage;
            form.validFields["name"] = false;
        } else {
            form.errors["name"] = false;
            form.validFields["name"] = true;
        }
        return this.isValid;
    },
    username: function (username) {
        this.isValid = /^[a-zA-Z]+[\w\.][a-zA-Z0-9]+$/
            .test(username);
        this.errorMessage = "Your name must be number, chars, and _ only.";
        if (!this.isValid) {
            form.errors["username"] = this.errorMessage;
            form.validFields["username"] = false;
        } else {
            form.errors["username"] = false;
            form.validFields["username"] = true;
        }
        return this.isValid;
    },
    email: function (email) {
        this.isValid = /^[a-zA-Z]+[\w\._+]+@([^\.]\w*\.)*[a-zA-Z]*[a-zA-Z]$/
            .test(email);
        this.error = "You must have a valid email address.";
        if (!this.isValid) {
            form.errors["email"] = this.errorMessage;
            form.validFields["email"] = false;
        } else {
            form.errors["email"] = false;
            form.validFields["email"] = true;
        }
        return this.isValid;
    },
    validFields: {
        name: false,
        username: false,
        email : false
    },
    errors: {
        name: false,
        username: false,
        email : false
    },
    isValid: function () {
        var hasInvalid;
        // check for false to be in our validFields obj.
        $jQ.each(form.validFields, function(index, value) {
            if (!value) {
                hasInvalid = true;
            }
        });
        // flip logic, because were checking for the existence, of false.
        return (hasInvalid ? false : true);
    },
};

function formHandler($e) {
    $e.each(function () {
        if (!form[this.name](this.value)) {
            $jQ(this).after(function () {
                    return '<div class="error">' + form.errors[this.name] + '</div>';
                });
        } else {
            $jQ(this).next('.error').remove();
        }
    });
    // validation over.
    console.log(form.isValid());
};

(function () {
    /*
     * @description make my error class.
     */

    this.sheet = document.styleSheets[0];
    this.errorStyle = (".error {" +
                       "background-color: tomato;" +
                       "color: #fff;" +
                       "size: .75em;" +
                       "padding: 10px;" +
                       "margin: 10px;" +
                       "border-radius: 5px; }");
    this.sheet.insertRule(this.errorStyle, 0);
}());
$jQ(function () {
    /*
     * @description event bindings.
     */
    $jQ('#signup').on({
        'submit': function(e){
            e.preventDefault();
            var toCheck = $jQ(e.target).children('input').not("#submit");
            formHandler(toCheck);
        },
        'change': function(e){
            var toCheck = $jQ(e.target);
            formHandler(toCheck);
        }
    });
}());