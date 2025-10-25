<template>
  <div style="max-width:520px;margin:40px auto;border:1px solid #ddd;padding:24px;">
    <h2 style="text-align:center;margin-bottom:16px;">REGISTRASI AKUN</h2>

    <div style="display:grid;grid-template-columns:130px 1fr;align-items:center;row-gap:10px;column-gap:8px;">
      <label style="text-align:start;">Nama Lengkap :</label>
      <input v-model="form.nama" placeholder="Nama lengkap" />

      <label style="text-align:start;">Email :</label>
      <input v-model="form.email" type="email" placeholder="nama@email.com" />

      <label style="text-align:start;">Username :</label>
      <input v-model="form.username" placeholder="username" />

      <label style="text-align:start;">Password :</label>
      <input v-model="form.password" type="password" placeholder="••••••••" />
    </div>


    <div style="display:flex;justify-content:center;gap:12px;margin-top:14px;">
      <button @click="onRegister" :disabled="loading">
        {{ loading ? "Memproses..." : "Registrasi" }}
      </button>
      <button @click="$router.push('/login')" :disabled="loading">Kembali ke Login</button>
    </div>

    <p v-if="msg" style="color:green;margin-top:10px;">{{ msg }}</p>
    <p v-if="error" style="color:red;margin-top:10px;">{{ error }}</p>
  </div>
</template>

<script setup>
import { reactive, ref } from "vue";
import api from "../services/api";
import { useRouter } from "vue-router";

const router = useRouter();
const form = reactive({ nama: "", email: "", username: "", password: "" });
const msg = ref(""); const error = ref("");

async function onRegister() {
  msg.value = ""; error.value = "";
  try {
    await api.post("/users/register", form);
    msg.value = "Registrasi berhasil";
    setTimeout(() => router.push("/login"), 800);
  } catch (e) {
    error.value = e?.response?.data?.message || "Gagal registrasi";
  }
}
</script>
