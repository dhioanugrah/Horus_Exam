<template>
  <div style="max-width:520px;margin:40px auto;border:1px solid #ddd;padding:24px;">
    <h2 style="text-align:center;margin-bottom:16px;">UPDATE USER</h2>

    <div style="display:grid;grid-template-columns:130px 1fr;align-items:center;row-gap:10px;column-gap:8px;">
      <label style="text-align:start;">Nama Lengkap :</label>
      <input v-model="form.nama" />

      <label style="text-align:start;">Email :</label>
      <input v-model="form.email" type="email" />

      <label style="text-align:start;">Username :</label>
      <input v-model="form.username" />
    </div>

    <div style="display:flex;justify-content:center;gap:12px;margin-top:14px;">
      <button @click="onUpdate" :disabled="loading">{{ loading ? 'Memproses...' : 'Update' }}</button>
      <button @click="$router.push('/dashboard')" :disabled="loading">Kembali</button>
    </div>

    <p v-if="msg" style="color:green;margin-top:10px;">{{ msg }}</p>
    <p v-if="error" style="color:red;margin-top:10px;">{{ error }}</p>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from "vue";
import api from "../services/api";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const id = Number(route.params.id);

const loading = ref(false);
const msg = ref("");
const error = ref("");

const form = reactive({ nama: "", email: "", username: "" });

onMounted(async () => {

  const st = history.state && history.state.user;
  if (st) {
    Object.assign(form, { nama: st.nama, email: st.email, username: st.username });
    return;
  }

  try {
    const { data } = await api.get("/users");
    const u = Array.isArray(data) ? data.find(x => Number(x.id) === id) : null;
    if (u) Object.assign(form, { nama: u.nama, email: u.email, username: u.username });
  } catch (e) {
    error.value = "Gagal memuat data user";
  }
});

async function onUpdate() {
  msg.value = ""; error.value = ""; loading.value = true;
  try {
    await api.put(`/users/${id}`, form);
    msg.value = "Data user berhasil diperbarui";
    setTimeout(() => router.push("/dashboard"), 600);
  } catch (e) {
    error.value = e?.response?.data?.message || "Gagal update";
  } finally {
    loading.value = false;
  }
}
</script>
