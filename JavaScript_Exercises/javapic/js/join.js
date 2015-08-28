/**
 * Created by Maxwell J. Resnick on 8/27/15.
 * join
 * ----
 * validate name
 * validate username
 * validate email
 * allow to submission, and redirect to the next page
 */


    function validate(e) {
        /*
         * @description validates form
         */
    this.fieldsToValidate = e;
    this.validation = null;
    if (this.fieldsToValidate.getAttribute('name') === 'name') {
        var name = /[a-z]*/.test(this.fieldsToValidate);
        if (!name) {
            this.validation = false;
        }
        this.validation = true;
    } else if (this.fieldsToValidate.getAttribute('name') === 'email') {
        var email = /^[a-z]+[\w\._+]+@([^\.]\w*+\.)*+[a-z]*/.test(this.fieldsToValidate.text);
        if (!email) {
            this.validation = false;
        }
        this.validation =  true;

    }
    console.log(this.validation);
}

// Event Binding
var form = document.getElementById('signup');
form.addEventListener('change', function(e){
    validate(e.target);
});