from pyscript import display, document

def place_order(e):
    #to prevent reload after clicking submit
    e.preventDefault()

    #to get items from checkboxes 
    # hi ms i didnt know how to get the cheked boxes so this was modified by chatGPT 
    # - prompt is "python how to get checked checkboxes" (i put the link in my docs)
    checked = document.querySelectorAll('input[name="menu"]:checked')
    if not checked:
        display("Please select an item!", target="sum")
        return
    items = [cb.nextSibling.nodeValue.strip() for cb in checked]
    total = sum(int(cb.value) for cb in checked)

    #to get customer info
    yn = document.getElementById("name").value
    add = document.getElementById("add").value
    num = document.getElementById("num").value

    #order summary text
    summary =f"""
    Order for: {yn} <br>
    Address: {add} <br>
    Contact Number: {num} <br>
    Items Ordered: {", ".join(items)} <br>
    Total: ₱{total} <br>
    Thank you for ordering at Kitty Coffee!"""

    #displaying order summary
    document.getElementById("sum").innerHTML = summary
