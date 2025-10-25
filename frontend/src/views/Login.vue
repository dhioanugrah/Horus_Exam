<template>
  <div style="max-width:420px;margin:40px auto;border:1px solid #ddd;padding:24px;">
    <h2 style="text-align:center;margin-bottom:16px;">LOGIN</h2>


    <div style="display:grid;grid-template-columns:100px 1fr;align-items:center;row-gap:10px;">
      <label style="text-align:start;">Username :</label>
      <input v-model="form.username" placeholder="username" />

      <label style="text-align:start;">Password :</label>
      <input v-model="form.password" type="password" placeholder="••••••••" />
    </div>


    <div style="display:flex;justify-content:center;gap:5px;margin-top:14px;">
      <button @click="onLogin" :disabled="loading">{{ loading ? "Memproses..." : "Login" }}</button>
      <button @click="$router.push('/register')" :disabled="loading">Registrasi</button>
    </div>

    <p v-if="error" style="color:red;margin-top:10px;">{{ error }}</p>
  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import api from "../services/api";
import { auth } from "../store/auth";
import { useRouter } from "vue-router";

const router = useRouter();
const form = reactive({ username: "", password: "" });
const error = ref("");

async function onLogin() {
  error.value = "";
  try {
    const { data } = await api.post("/users/login", form);
    auth.setToken(data.token);
    router.push("/dashboard");
  } catch (e) {
    error.value = e?.response?.data?.message || "Gagal login";
  }
}
</script>
