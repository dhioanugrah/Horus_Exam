<template>
  <div style="max-width:900px;margin:24px auto;">
    <h2>DASHBOARD PENGGUNA</h2>
    <SearchBar @on-search="onSearch"/>
    <UserTable :users="filtered" @update="goUpdate" @delete="onDelete"/>
    <div style="margin-bottom:12px; margin-top:12px; text-align:right;">
      <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import api from "../services/api";
import { auth } from "../store/auth";
import SearchBar from "../components/SearchBar.vue";
import UserTable from "../components/UserTable.vue";
import { useRouter } from "vue-router";

const router = useRouter();
const users = ref([]);
const q = ref("");

const filtered = computed(() => {
  if (!q.value) return users.value;
  const s = q.value.toLowerCase();
  return users.value.filter(u =>
    (u.nama || "").toLowerCase().includes(s) ||
    (u.username || "").toLowerCase().includes(s)
  );
});

function onSearch(val) { q.value = val; }

async function load() {
  const { data } = await api.get("/users");
  users.value = data;
}

function logout() {
  auth.clear();
  router.push("/login");
}

function goUpdate(u) {
  router.push({ name: "UpdateUser", params: { id: u.id }, state: { user: u } });
}

async function onDelete(u) {
  const ok = confirm(`Apakah Anda yakin hapus ${u.username}?`);
  if (!ok) return;
  await api.delete(`/users/${u.id}`);
  await load();
}

onMounted(load);
</script>
