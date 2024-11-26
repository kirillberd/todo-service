<script lang="ts">
import { defineComponent, ref } from 'vue';
import TaskPage from './components/TaskPage.vue';
import type { Task } from './models/task';

export default defineComponent({
  name: 'App',
  
  components: {
    TaskPage
  },
  
  setup() {
    const tasks = ref<Task[]>([]);

    const handleSaveTask = (task: Task) => {
      if (task.id === null) {
        task.id = Date.now();
      }
      tasks.value.push(task);
    };

    return {
      tasks,
      handleSaveTask
    };
  }
});
</script>

<template>
  <div>
    <TaskPage @save-task="handleSaveTask" />
    <!-- Остальной контент -->
  </div>
</template>