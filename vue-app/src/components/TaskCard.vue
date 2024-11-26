<script lang="ts">
import { defineComponent, PropType } from 'vue';
import type { Task } from '../models/task';

export default defineComponent({
  name: 'TaskCard',
  
  props: {
    task: {
      type: Object as PropType<Task>,
      required: true
    }
  },

  emits: ['close', 'delete'],

  setup(props, { emit }) {
    const handleDelete = () => {
      if (confirm('Вы уверены, что хотите удалить эту задачу?')) {
        emit('delete', props.task.id);
      }
    };

    return {
      handleDelete
    };
  }
});
</script>

<template>
  <div class="task-card">
    <div class="task-card__header">
      <h2>{{ task.name }}</h2>
      <button class="close-button" @click="$emit('close')">×</button>
    </div>

    <div class="task-card__body">
      <div class="info-group">
        <label>Статус</label>
        <span class="task-state" :class="task.state">{{ task.state }}</span>
      </div>

      <div class="info-group" v-if="task.deadline">
        <label>Дедлайн</label>
        <span>{{ new Date(task.deadline).toLocaleString() }}</span>
      </div>

      <div class="info-group" v-if="task.tags?.size">
        <label>Теги</label>
        <div class="tags-container">
          <span
            v-for="tag in task.tags"
            :key="tag"
            class="tag"
          >
            {{ tag }}
          </span>
        </div>
      </div>

      <div class="info-group" v-if="task.comments">
        <label>Комментарии</label>
        <p class="comments">{{ task.comments }}</p>
      </div>

      <div class="info-group">
        <label>Создано</label>
        <span>{{ new Date(task.created_at!).toLocaleString() }}</span>
      </div>
    </div>

    <div class="task-card__footer">
      <button
        class="button button--danger"
        @click="handleDelete"
      >
        Удалить задачу
      </button>
    </div>
  </div>
</template>
<style lang="scss" scoped>
@import "../assets/components/task-card.scss";
</style>