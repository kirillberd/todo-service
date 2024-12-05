<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import type { Task } from '../models/task';
import taskService from '../services/api/task-service';
import TaskForm from './TaskForm.vue';
import TaskCard from './TaskCard.vue';

export default defineComponent({
  name: 'TaskList',
  components: {
    TaskForm,
    TaskCard
  },

  setup() {
    const tasks = ref<Task[]>([]);
    const isLoading = ref(true);
    const error = ref<string | null>(null);
    const showTaskForm = ref(false);
    const selectedTask = ref<Task | null>(null);

    const loadTasks = async () => {
      try {
        isLoading.value = true;
        error.value = null;
        tasks.value = await taskService.getTasks();
      } catch (err) {
        error.value = 'Ошибка при загрузке задач';
        console.error(err);
      } finally {
        isLoading.value = false;
      }
    };

    const handleTaskCreate = async (task: Task) => {
      try {
        const newTask = await taskService.createTask(task);
        tasks.value.unshift(newTask);
        showTaskForm.value = false;
      } catch (err) {
        error.value = 'Ошибка при создании задачи';
        console.error(err);
      }
    };

    const handleTaskDelete = async (taskId: number) => {
      try {
        await taskService.deleteTask(taskId);
        tasks.value = tasks.value.filter(task => task.id !== taskId);
        selectedTask.value = null;
      } catch (err) {
        error.value = 'Ошибка при удалении задачи';
        console.error(err);
      }
    };

    const handleTaskSelect = (task: Task) => {
      selectedTask.value = task;
    };

    const closeModal = (e: MouseEvent) => {
      if ((e.target as HTMLElement).classList.contains('modal-overlay')) {
        showTaskForm.value = false;
        selectedTask.value = null;
      }
    };

    onMounted(loadTasks);

    return {
      tasks,
      isLoading,
      error,
      showTaskForm,
      selectedTask,
      handleTaskCreate,
      handleTaskDelete,
      handleTaskSelect,
      closeModal
    };
  }
});
</script>

<template>
  <div class="task-list-container">
    <!-- Заголовок -->
    <div class="header">
      <h1>Мои задачи</h1>
      <button
        @click="showTaskForm = true"
        class="button button--primary"
      >
        + Добавить задачу
      </button>
    </div>

    <!-- Отображение ошибки -->
    <div v-if="error" class="error-message">
      {{ error }}
    </div>

    <!-- Загрузка -->
    <div v-if="isLoading" class="loading">
      Загрузка задач...
    </div>

    <!-- Список задач -->
    <div v-else-if="tasks.length" class="tasks-grid">
      <div
        v-for="task in tasks"
        :key="task.id"
        class="task-item"
        @click="handleTaskSelect(task)"
        :class="{ 'selected': selectedTask?.id === task.id }"
      >
        <h3>{{ task.name }}</h3>
        <div class="task-meta">
          <span class="task-state" :class="task.state">{{ task.state }}</span>
          <span v-if="task.deadline" class="task-deadline">
            {{ new Date(task.deadline).toLocaleDateString() }}
          </span>
        </div>
        <div class="task-tags">
          <span
            v-for="tag in task.tags"
            :key="tag"
            class="tag"
          >
            {{ tag }}
          </span>
        </div>
      </div>
    </div>

    <!-- Пустое состояние -->
    <div v-else class="empty-state">
      Задач пока нет. Создайте новую задачу!
    </div>

    <!-- Модальное окно для создания задачи -->
    <Transition name="fade">
      <div v-if="showTaskForm" class="modal-overlay" @click="closeModal">
        <Transition name="slide-up">
          <div class="modal-container">
            <TaskForm
              @save-task="handleTaskCreate"
              @cancel="showTaskForm = false"
            />
          </div>
        </Transition>
      </div>
    </Transition>

    <!-- Модальное окно для просмотра задачи -->
    <Transition name="fade">
      <div v-if="selectedTask" class="modal-overlay" @click="closeModal">
        <Transition name="slide-up">
          <div class="modal-container">
            <TaskCard
              :task="selectedTask"
              @close="selectedTask = null"
              @delete="handleTaskDelete"
            />
          </div>
        </Transition>
      </div>
    </Transition>
  </div>
</template>
<style lang="scss" scoped>
@import "../assets/components/task-list.scss";
</style>