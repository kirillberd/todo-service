<script lang="ts">
import { defineComponent, ref } from 'vue';
import type { Task } from '../models/task';

export default defineComponent({
  name: 'TaskForm',
  
  emits: {
    'save-task': (task: Task) => true,
    'cancel': () => true
  },
  
  setup(_, { emit }) {
    const initialTask: Task = {
      user_id: '',
      name: '',
      tags: [],
      comments: null,
      state: 'new',
      deadline: null,
    };

    const task = ref<Task>({ ...initialTask });
    const newTag = ref('');
    const errors = ref<Record<string, string>>({});
    const isLoading = ref(false);

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
          task.value.tags = [];
        }
        if (!task.value.tags.includes(newTag.value.trim())) {
          task.value.tags.push(newTag.value.trim());
        }
        newTag.value = '';
      }
    };

    const removeTag = (tagToRemove: string) => {
      if (task.value.tags) {
        task.value.tags = task.value.tags.filter(tag => tag !== tagToRemove);
        if (task.value.tags.length === 0) {
          task.value.tags = null;
        }
      }
    };

    const handleTagKeydown = (e: KeyboardEvent) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        addTag();
      }
    };

    const handleSubmit = async () => {
      if (validateForm()) {
        try {
          isLoading.value = true;
          
          const submittedTask = {
            ...task.value,
          };
          
          emit('save-task', submittedTask);
          task.value = { ...initialTask };
          
        } catch (error) {
          console.error('Error creating task:', error);
        } finally {
          isLoading.value = false;
        }
      }
    };

    const handleCancel = () => {
      task.value = { ...initialTask };
      errors.value = {};
      emit('cancel');
    };

    return {
      task,
      newTag,
      errors,
      isLoading,
      addTag,
      removeTag,
      handleSubmit,
      handleCancel,
      handleTagKeydown
    };
  }
});
</script>

<template>
  <div class="task-form-card" @click.stop>
    <div class="task-form-card__header">
      <h2>Создание задачи</h2>
      <button 
        class="close-button"
        @click="handleCancel"
        :disabled="isLoading"
      >
        ×
      </button>
    </div>
    
    <div class="task-form-card__content">
      <form @submit.prevent="handleSubmit" class="task-form">
        <div class="form-group">
          <label>Название задачи*</label>
          <input
            v-model="task.name"
            type="text"
            class="input-field"
            :class="{ 'input-field--error': errors.name }"
            :disabled="isLoading"
            placeholder="Введите название задачи"
          />
          <span v-if="errors.name" class="error-message">
            {{ errors.name }}
          </span>
        </div>

        <div class="form-group">
          <label>Дедлайн</label>
          <input
            v-model="task.deadline"
            type="datetime-local"
            class="input-field"
            :disabled="isLoading"
          />
        </div>

        <div class="form-group">
          <label>Теги</label>
          <div class="tags-input">
            <input
              v-model="newTag"
              type="text"
              class="input-field"
              placeholder="Введите тег и нажмите Enter"
              @keydown="handleTagKeydown"
              :disabled="isLoading"
            />
            <button
              type="button"
              class="button button--secondary tag-button"
              @click="addTag"
              :disabled="isLoading || !newTag.trim()"
            >
              +
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
                class="tag-remove"
                @click="removeTag(tag)"
                :disabled="isLoading"
              >
                ×
              </button>
            </span>
          </div>
        </div>

        <div class="form-group">
          <label>Комментарии</label>
          <textarea
            v-model="task.comments"
            rows="3"
            class="input-field"
            :disabled="isLoading"
            placeholder="Добавьте комментарии к задаче"
          ></textarea>
        </div>

        <div class="form-actions">
          <button
            type="button"
            class="button button--secondary"
            @click="handleCancel"
            :disabled="isLoading"
          >
            Отмена
          </button>
          <button
            type="submit"
            class="button button--primary"
            :disabled="isLoading"
          >
            {{ isLoading ? 'Сохранение...' : 'Создать задачу' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '../assets/components/task-form.scss';
</style>