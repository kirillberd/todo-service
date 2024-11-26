<script lang="ts">
import { defineComponent, ref } from 'vue';
import type { Task } from '../models/task';
import "../assets/task_page_style.scss";

export default defineComponent({
  name: 'TaskPage',
  
  emits: {
    'save-task': (task: Task) => true
  },
  
  setup(props, { emit }) {
    const initialTask: Task = {
      id: null,
      user_id: '',
      name: '',
      tags: new Set<string>(),
      comments: null,
      created_at: null,
      state: 'new',
      deadline: null,
    };

    const task = ref<Task>({ ...initialTask });
    const newTag = ref('');
    const errors = ref<Record<string, string>>({});

    const validateForm = (): boolean => {
      errors.value = {};
      
      if (!task.value.name.trim()) {
        errors.value.name = 'Название задачи обязательно';
      }

      return Object.keys(errors.value).length === 0;
    };

    const addTag = () => {
      if (newTag.value.trim()) {
        if (!task.value.tags) {
          task.value.tags = new Set<string>();
        }
        task.value.tags.add(newTag.value.trim());
        newTag.value = '';
      }
    };

    const removeTag = (tag: string) => {
      task.value.tags?.delete(tag);
    };

    const handleSubmit = () => {
      if (validateForm()) {
        const submittedTask = {
          ...task.value,
          created_at: new Date().toISOString(),
          state: 'new',
          user_id: 'default_user'
        };
        
        emit('save-task', submittedTask);
        task.value = { ...initialTask };
      }
    };

    const resetForm = () => {
      task.value = { ...initialTask };
      errors.value = {};
    };

    return {
      task,
      newTag,
      errors,
      addTag,
      removeTag,
      handleSubmit,
      resetForm
    };
  }
});
</script>

<template>
  <div class="task-card">
    <div class="task-card__header">
      <h1>Создание задачи</h1>
    </div>
    
    <div class="task-card__body">
      <form @submit.prevent="handleSubmit" class="task-form">
        <!-- Название задачи -->
        <div class="task-form__group">
          <label>Название задачи*</label>
          <input
            v-model="task.name"
            type="text"
            class="input-field"
            :class="{ 'input-field--error': errors.name }"
          />
          <span v-if="errors.name" class="error-message">{{ errors.name }}</span>
        </div>

        <!-- Дедлайн -->
        <div class="task-form__group">
          <label>Дедлайн</label>
          <input
            v-model="task.deadline"
            type="datetime-local"
            class="input-field"
          />
        </div>

        <!-- Теги -->
        <div class="task-form__group">
          <label>Теги</label>
          <div class="flex gap-2">
            <input
              v-model="newTag"
              type="text"
              class="input-field flex-grow"
              placeholder="Добавить тег"
              @keyup.enter.prevent="addTag"
            />
            <button
              type="button"
              @click="addTag"
              class="button button--primary"
            >
              Добавить
            </button>
          </div>
          <div class="tags-container">
            <span
              v-for="tag in task.tags"
              :key="tag"
              class="tag"
            >
              {{ tag }}
              <button
                type="button"
                class="tag__remove"
                @click="removeTag(tag)"
              >
                ×
              </button>
            </span>
          </div>
        </div>

        <!-- Комментарии -->
        <div class="task-form__group">
          <label>Комментарии</label>
          <textarea
            v-model="task.comments"
            rows="3"
            class="input-field"
          ></textarea>
        </div>

        <!-- Кнопки -->
        <div class="buttons-container">
          <button
            type="submit"
            class="button button--primary"
          >
            Сохранить
          </button>
          <button
            type="button"
            @click="resetForm"
            class="button button--secondary"
          >
            Сбросить
          </button>
        </div>
      </form>
    </div>
  </div>
</template>