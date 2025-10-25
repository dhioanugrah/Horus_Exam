import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Dashboard from "../views/Dashboard.vue";
import UpdateUser from "../views/UpdateUser.vue";

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", name: "Login", component: Login, meta: { guest: true } },
  { path: "/register", name: "Register", component: Register, meta: { guest: true } },
  { path: "/dashboard", name: "Dashboard", component: Dashboard, meta: { requiresAuth: true } },
  { path: "/update/:id", name: "UpdateUser", component: UpdateUser, meta: { requiresAuth: true } }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

router.beforeEach((to, _from, next) => {
  const token = localStorage.getItem("token");
  if (to.meta.requiresAuth && !token) return next({ name: "Login" });
  if (to.meta.guest && token) return next({ name: "Dashboard" });
  next();
});

export default router;
