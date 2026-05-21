document.getElementById("add-btn").addEventListener("click", function() {
    var taskInput = document.getElementById("todo-input");
    var taskText = taskInput.value;
    if (taskText === "") {
        alert("Please enter a task.");
    } else {
        var li = document.createElement("li");
        li.appendChild(document.createTextNode(taskText));
        document.getElementById("todo-list").appendChild(li);
        taskInput.value = "";
    }
});
