function addTask() {
  const title = document.getElementById("taskTitle").value.trim();
  const date = document.getElementById("taskDate").value;
  const time = document.getElementById("taskTime").value;

  if (!title || !date || !time) {
    alert("Please fill all fields.");
    return;
  }

  const taskList = document.getElementById("taskList");

  const li = document.createElement("li");

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.onchange = () => {
    li.classList.toggle("completed", checkbox.checked);
  };

  const infoDiv = document.createElement("div");
  infoDiv.className = "task-info";

  const titleSpan = document.createElement("div");
  titleSpan.className = "task-title";
  titleSpan.textContent = title;

  const timeSpan = document.createElement("div");
  timeSpan.className = "task-time";
  timeSpan.textContent = `${date} at ${time}`;

  infoDiv.appendChild(titleSpan);
  infoDiv.appendChild(timeSpan);

  const delBtn = document.createElement("button");
  delBtn.textContent = "🗑️";
  delBtn.className = "delete-btn";
  delBtn.onclick = () => {
    taskList.removeChild(li);
  };

  li.appendChild(checkbox);
  li.appendChild(infoDiv);
  li.appendChild(delBtn);

  taskList.appendChild(li);

  // Clear fields
  document.getElementById("taskTitle").value = "";
  document.getElementById("taskDate").value = "";
  document.getElementById("taskTime").value = "";
}
