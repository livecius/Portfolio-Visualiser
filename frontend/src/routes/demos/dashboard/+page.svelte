<script>
  import { Chart } from "svelte-echarts";

  import { init, use } from 'echarts/core'
  import { PieChart } from 'echarts/charts'
  import { GridComponent, TitleComponent } from "echarts/components";
  import { CanvasRenderer } from "echarts/renderers";

  use([PieChart, GridComponent, CanvasRenderer, TitleComponent])

  let options = {
      tooltip: {
          trigger: 'item',
      },
      series: [
          {
              name: 'Ownership of',
              type: 'pie',
              radius: '50%',
              color: [
                  '#000000',
                  '#474747',
                  '#676767',
                  '#a5a5a5',
                  '#c1c1c1',
              ],
              data: [
                  { value: 1048, name: 'Nvidia (NVDA)' },
                  { value: 735, name: 'Amazon (AMZN)' },
                  { value: 580, name: 'Apple (AAPL)' },
                  { value: 484, name: 'United States Dollar (USD)' },
                  { value: 300, name: 'Advanced Micro Devices  (AMD)' }
              ],
              emphasis: {
                  itemStyle: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: 'rgba(0,0,0,0.5)'
                  }
              }
          }
      ]
  }
</script>

<style>
  .app {
      width: 60vh;
      height: 60vh;
  }
</style>

<!-- Navbar -->
<div class="navbar bg-base-100 shadow-sm">
  <div class="navbar-start">
    <div class="dropdown">
      <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" /> </svg>
      </div>
      <ul
        tabindex="0"
        class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 glass">
        <li><a class="font-bold text-xl" href="/demos/dashboard">Dashboard</a></li>
      </ul>
    </div>
  </div>

  <div class="navbar-center">
    <p class="text-xl">Your Portfolio</p>
  </div>

  <div class="navbar-end">
    <ul class="menu menu-horizontal px-1">
      <li>
        <a class="" href="/">Log Out
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
            <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
          </svg>
        </a>
      </li>
    </ul>
  </div>
</div>

<!-- First Section: Pie Chart & Total Portfolio Value -->
<div>
  <div class="flex w-full">
    <div class="app">
      <Chart {init} {options} />
    </div>

    <div>
      <table class="table">
        <!-- Head -->
        <thead>
          <tr>
            <th>Asset Name</th>
            <th>Total Value</th>
            <th>Allocation</th>
          </tr>
        </thead>
        <!-- Row -->
        <tbody>
          <tr>
            <th>🏛️ Nvidia</th>
            <th>$2,841.23</th>
            <th>33.30%</th>
          </tr>
        </tbody>
        <tbody>
          <tr>
            <th>🏛️ Amazon</th>
            <th>$1,993.13</th>
            <th>23.36%</th>
          </tr>
        </tbody>
        <tbody>
          <tr>
            <th>🏛️ Apple</th>
            <th>$1,572.49</th>
            <th>18.43%</th>
          </tr>
        </tbody>
        <tbody>
          <tr>
            <th>💲 United States Dollar</th>
            <th>$1,312.26</th>
            <th>15.38%</th>
          </tr>
        </tbody>
        <tbody>
          <tr>
            <th>🏛️ Advanced Micro Devices</th>
            <th>$813.12</th>
            <th>9.53%</th>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="divider divider-horizontal"></div>
    <!-- Total Portfolio Value -->

    <div class="stats shadow">
      <div class="stat">
        <div class="stat-title">Total Portfolio Value</div>
        <div class="stat-value">$8,532.25</div>
        <div class="stat-desc text-success">↗︎ $103.43 This Week (1.21%)</div>
      </div>

      <div class="stat">
        <div class="stat-title">Total Dividends Received</div>
        <div class="stat-value">$32.56</div>
        <div class="stat-desc">Average of $1.52 a month.</div>
      </div>

      <div class="stat">
        <div class="stat-title">Total Unrealised Gains</div>
        <div class="stat-value">$1,562.42</div>
        <div class="stat-desc text-success">↗ $23.56 since yesterday!</div>
      </div>
    </div>
  </div>
</div>

<div class="divider divider-vertical"></div>