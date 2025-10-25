<template>
  <table border="1" cellpadding="6" cellspacing="0" width="100%">
    <thead>
      <tr>
        <th>ID</th><th>Username</th><th>Nama Lengkap</th><th>Email</th><th>Aksi</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="u in users" :key="u.id">
        <td>{{ u.id }}</td>
        <td>{{ u.username }}</td>
        <td>{{ u.nama }}</td>
        <td>{{ u.email }}</td>
        <td style="text-align:center;">
          <button @click="$emit('update', u)">U</button>
          <button style="margin-left:2px;" @click="$emit('delete', u)">H</button>
        </td>
      </tr>
      <tr v-if="!users || users.length === 0">
        <td colspan="5">Tidak ada data</td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
defineProps({ users: { type: Array, default: () => [] } });
</script>
