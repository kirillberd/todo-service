<!-- views/TaskPage.vue -->
<template>
    <div class="task-page">
      <div class="task-page__header">
        <h1 class="task-page__title">Мои задачи</h1>
        <button class="btn-create" @click="showCreateModal = true">
          Создать задачу
        </button>
      </div>
  
      <div v-if="loading" class="task-page__loading">
        Загрузка...
      </div>
      
      <div v-else-if="error" class="task-page__error">
        {{ error }}
      </div>
      
      <TaskList
        v-else
        :tasks="tasks"
        @edit="handleEdit"
        @delete="handleDelete"
      />
  
      <!-- Модальное окно -->
      <div v-if="showCreateModal" class="modal-overlay" @click="handleModalClose">
        <div class="modal-content" @click.stop>
          <TaskForm 
            @submit="handleTaskCreate" 
            @cancel="showCreateModal = false"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, onMounted, ref } from 'vue';
  import { taskService, TaskResponse } from '../services/taskService';
  import TaskList from '../components/TaskList.vue';
  import TaskForm from '../components/TaskForm.vue';
  
  export default defineComponent({
    name: 'TaskPage',
    components: {
      TaskList,
      TaskForm
    },
    setup() {
      const tasks = ref<TaskResponse[]>([]);
      const loading = ref(true);
      const error = ref('');
      const showCreateModal = ref(false);
  
      const loadTasks = async () => {
        try {
          loading.value = true;
          tasks.value = await taskService.getTasks();
        } catch (err: any) {
          error.value = err.message;
        } finally {
          loading.value = false;
        }
      };
  
      const handleEdit = (task: TaskResponse) => {
        // Логика редактирования
      };
  
      const handleDelete = async (taskId: number) => {
        if (confirm('Вы уверены, что хотите удалить задачу?')) {
          try {
            await taskService.deleteTask(taskId);
            await loadTasks();
          } catch (err: any) {
            error.value = err.message;
          }
        }
      };
  
      const handleTaskCreate = async (taskData: any) => {
        try {
          await taskService.createTask(taskData);
          showCreateModal.value = false;
          await loadTasks();
        } catch (err: any) {
          error.value = err.message;
        }
      };
  
      const handleModalClose = (e: MouseEvent) => {
        if (e.target === e.currentTarget) {
          showCreateModal.value = false;
        }
      };
  
      onMounted(loadTasks);
  
      return {
        tasks,
        loading,
        error,
        showCreateModal,
        handleEdit,
        handleDelete,
        handleTaskCreate,
        handleModalClose
      };
    }
  });
  </script>
  <style src="src/assets/components/task-page.scss"></style>
