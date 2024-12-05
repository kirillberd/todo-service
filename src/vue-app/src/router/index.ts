import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from "../store/userStore";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import TaskForm from '../components/TaskForm.vue'
const routes = [
  {

    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/register",
    name: "register",
    component: Register,
  },
  {
    path: '/',
    name: 'task-from',
    component: TaskForm,
    meta: { requiresAuth: true } // добавляем мета-поле для проверки аутентификации
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
  if (requiresAuth && !userStore.isAuthenticated) {

    next("/login");
  } else {
    next();
  }
});

export default router;
