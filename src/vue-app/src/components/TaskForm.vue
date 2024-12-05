<template>
  <div class="task-form-container">
    <h2 class="form-title">Новая задача</h2>
    <form @submit.prevent="handleSubmit" class="task-form">
      <div class="form-group">
        <label for="name">Название задачи*</label>
        <input 
          id="name"
          v-model="taskData.name"
          type="text"
          required
          class="form-input"
          placeholder="Введите название задачи"
        />
      </div>

      <div class="form-group">
        <label for="tags">Теги</label>
        <div class="tags-input-container">
          <input 
            id="tags"
            v-model="tagInput"
            type="text"
            class="form-input"
            placeholder="Добавьте теги"
            @keydown.enter.prevent="addTag"
          />
          <button type="button" class="add-tag-btn" @click="addTag">+</button>
        </div>
        <div class="tags-container" v-if="taskData.tags.length">
          <span v-for="(tag, index) in taskData.tags" :key="index" class="tag">
            {{ tag }}
            <button type="button" class="remove-tag" @click="removeTag(index)">×</button>
          </span>
        </div>
      </div>

      <div class="form-group">
        <label for="state">Статус*</label>
        <select id="state" v-model="taskData.state" required class="form-select">
          <option value="new">Новая</option>
          <option value="in_progress">В работе</option>
          <option value="completed">Завершена</option>
        </select>
      </div>

      <div class="form-group">
        <label for="deadline">Дедлайн</label>
        <input 
          id="deadline"
          v-model="taskData.deadline"
          type="datetime-local"
          class="form-input"
        />
      </div>

      <div class="form-group">
        <label for="comments">Комментарии</label>
        <textarea 
          id="comments"
          v-model="taskData.comments"
          class="form-textarea"
          placeholder="Добавьте комментарии к задаче"
        ></textarea>
      </div>

      <div class="form-actions">
        <button type="button" class="btn-cancel" @click="$emit('cancel')">Отмена</button>
        <button type="submit" class="btn-submit">Создать задачу</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from 'vue';
import { useUserStore } from '../store/userStore';

interface TaskData {
  name: string;
  tags: string[];
  state: string;
  comments: string;
  deadline: string;
}

export default defineComponent({
  name: 'TaskForm',
  emits: ['submit', 'cancel'],
  setup(_, { emit }) {
    const userStore = useUserStore();
    const tagInput = ref('');

    const taskData = reactive<TaskData>({
      name: '',
      tags: [],
      state: 'new',
      comments: '',
      deadline: ''
    });

    const addTag = () => {
      if (tagInput.value.trim()) {
        taskData.tags.push(tagInput.value.trim());
        tagInput.value = '';
      }
    };

    const removeTag = (index: number) => {
      taskData.tags.splice(index, 1);
    };

    const handleSubmit = () => {
      const submitData = {
        ...taskData,
        user_id: userStore.user?.id,
        created_at: new Date(),
        deadline: taskData.deadline ? new Date(taskData.deadline) : null
      };
    };

    return {
      taskData,
      tagInput,
      addTag,
      removeTag,
      handleSubmit
    };
  }
});
</script>

<style lang="scss" src="src/assets/components/task-form.scss"></style>