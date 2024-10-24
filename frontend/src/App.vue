<template>
  <div>
    <el-button type="primary" size="default" :icon="Plus">点我吧</el-button>
    <br>
    <el-button type="danger" size="default" :icon="Plus">点我吧</el-button>
    <el-calendar v-model="value" />
    <el-carousel trigger="click" height="150px">
        <el-carousel-item> container1 </el-carousel-item>
        <el-carousel-item> container2 </el-carousel-item>
        <el-carousel-item> container3 </el-carousel-item>
    </el-carousel>
    <el-date-picker v-model="value" type="date" placeholder="请选择日期" />
    <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/' }">homepage</el-breadcrumb-item>
        <el-breadcrumb-item><a href="/">promotion management</a></el-breadcrumb-item>
        <el-breadcrumb-item>promotion list</el-breadcrumb-item>
        <el-breadcrumb-item>promotion detail</el-breadcrumb-item>
    </el-breadcrumb>
    <el-pagination
        v-model:current-page="currentPage"
        v-model:page-size="pageSize"
        :page-sizes="[100, 200, 300, 400]"
        background
        layout="total, sizes, prev, pager, next, jumper"
        :total="400"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
    />
    <el-tag :style="{ marginRight: '6px' }">Tag 1</el-tag>
    <el-tag :style="{ marginRight: '6px' }" type="success">Tag 2</el-tag>
    <el-tag :style="{ marginRight: '6px' }" type="info">Tag 3</el-tag>
    <el-tag :style="{ marginRight: '6px' }" type="warning">Tag 4</el-tag>
    <el-tag :style="{ marginRight: '6px' }" type="danger">Tag 5</el-tag>
  <el-dialog v-model="show" title="Shipping address">
      <main>container</main>
      <template #footer>
          <span class="dialog-footer">
              <el-button @click="show = false">Cancel</el-button>
              <el-button type="primary" @click="show = false"> Confirm </el-button>
          </span>
      </template>
  </el-dialog>
  <el-date-picker v-model="value" type="daterange" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期" />
  <br>
  <el-date-picker v-model="value" type="month" placeholder="请选择月份" />
  <el-image :src="url" :preview-src-list="[url]" fit="cover" />
  <el-select v-model="value" multiple collapse-tags placeholder="请选择">
      <el-option label="Options1" value="1" />
      <el-option label="Options2" value="2" />
  </el-select>
  <el-table :data="tableData" style="width: 100%">
    <el-calendar v-model="value" />
  </el-table>
  </div>
</template>

<script setup lang="ts">
import {Plus} from '@element-plus/icons-vue'

</script>

<style scoped></style>
