

import type { Task } from '../../models/task';
import axios from './axios-instance';

export class TaskService {
  private static instance: TaskService;
  private readonly baseUrl = '/tasks';

  private constructor() {}

  public static getInstance(): TaskService {
    if (!TaskService.instance) {
      TaskService.instance = new TaskService();
    }
    return TaskService.instance;
  }

  async createTask(task: Task): Promise<Task> {
    try {
      const { data } = await axios.post<Task>(this.baseUrl + '/add', task);
      return data;
    } catch (error) {
      throw error;
    }
  }

  async updateTask(task: Task): Promise<Task> {
    try {
      const { data } = await axios.put<Task>(`${this.baseUrl}/${task.id}`, task);
      return data;
    } catch (error) {
      throw error;
    }
  }

  async deleteTask(taskId: number): Promise<void> {
    try {
      await axios.delete(`${this.baseUrl}/${taskId}`);
    } catch (error) {
      throw error;
    }
  }

  async getTasks(): Promise<Task[]> {
    try {
      const { data } = await axios.get<Task[]>(this.baseUrl);
      return data;
    } catch (error) {
      throw error;
    }
  }

  async getTaskById(taskId: number): Promise<Task> {
    try {
      const { data } = await axios.get<Task>(`${this.baseUrl}/${taskId}`);
      return data;
    } catch (error) {
      throw error;
    }
  }

}

export default TaskService.getInstance();