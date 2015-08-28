/**
 * Created by Maxwell J. Resnick on 8/27/15.
 * join
 * ----
 * validate name
 * validate username
 * validate email
 * allow to submission, and redirect to the next page
 */


function assertMessage (target, message) {
    /*
     * @param takes HTMLCollection object, to attach sibling message to
     * @param the message.
     */
    this.target = target;
    this.message = message;

    var newMessageBlock = document.createElement('div');
    var messageText = document.createTextNode(this.message);
    newMessageBlock.appendChild(messageText);
    this.target.parentNode.insertBefore(newMessageBlock, this.target.nextSibling);
}
function checkFields(targets) {
    this.fieldsToValidate = targets;
    for (var i=0; i < this.fieldsToValidate.length; i++) {
        if (this.fieldsToValidate[i].getAttribute('name') === 'name') {
            // REGEX
            var name = /^[a-zA-Z]+[a-zA-Z ]+[a-zA-Z]$/
                .test(this.fieldsToValidate[i].value);
            // Going to explicitly test for true and false. What if it's all janky?
            if (!name) {
               this.errorMessage = "The name field must only contain Alphabet characters";
                assertMessage(this.fieldsToValidate[i], this.errorMessage);
                return false;
            } else if (name) {
                return true;
            }
        }
        else if (this.fieldsToValidate[i].getAttribute('name') === 'email') {
            /*
             * ^[a-zA-Z] - email usernamesstart w/ alpha only
             * [\w\._+] any alphanumeric but also "." "_" "+" are valid specials for usernames.
             * must be a @
             * any number of domains, subdomains as long as we end with a char.
             */
            var email = /^[a-zA-Z]+[\w\._+]+@([^\.]\w*\.)*[a-zA-Z]*[a-zA-Z]$/
                .test(this.fieldsToValidate[i].value);
            if (!email) {
                // TODO add html div with error message.
                return false;
            } else if (email) {
                return true;
            }

        }
        else if (this.fieldsToValidate[i].getAttribute('name') === 'username') {
            // REGEX
            var username = /^[a-zA-Z]+[\w\.][a-zA-Z0-9]$/
                .test(this.fieldsToValidate[i].value);
            if (!username) {
                // TODO add html div with error message.
                return false;
            } else if (username){
                return true;
            }
        }
    }
}
function validateForm(target, fullForm) {
    /*
     * @description validates form
     */
    this.fieldsToValidate = target;
    this.fullForm = fullForm;
    if (this.fullForm) {
        // get array of fields to validatem, cut the last once it's just the input button.
        this.toValidate = this.fieldsToValidate.target.getElementsByTagName('input');
        this.isValid = checkFields(this.toValidate);
    }
    else {
        this.toValidate = [this.fieldsToValidate.target];
        // we don't set this.isValid b.c. we don't care if a field is validated, that's just for UX.
        checkFields(this.toValidate);
    }
    console.log(this.isValid);
}
// TODO disable submit until all fields are valid, but this requires, maintaining a valid fields array... much more work.
// Event Binding
var form = document.getElementById('signup');
form.addEventListener('change', function(e){
    validateForm(e, false);
});
form.addEventListener('submit', function(e){
    validateForm(e, true);
});