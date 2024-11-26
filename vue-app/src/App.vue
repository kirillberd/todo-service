<script lang="ts">
import { defineComponent, ref } from 'vue';
import TaskPage from './components/TaskList.vue';
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
<style lang="scss">
.app {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    rgba(26, 28, 32, 0.95) 0%, 
    rgba(44, 47, 51, 0.95) 100%
  );
}
</style>