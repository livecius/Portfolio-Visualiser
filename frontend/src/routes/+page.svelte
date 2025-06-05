<style>
    .background {
        background-image: url("warrenbogle.png");
        background-size: cover;
        background-position: center;
        height: 100vh;
        width: 100%;
    }
</style>

<div class="background">
    <div class="hero min-h-screen">
        <div class="hero-content">
            <div class="card bg-base-300 w-full max-w-sm shrink-0 shadow-2xl">
                <div class="card-body rounded bg-transparent">
                    <p class="text-3xl font-extrabold text-center">Portfolio Visualiser</p>

                    <fieldset class="fieldset">
                        <label class="label">Email</label>
                        <input type="email" class="input" placeholder="Email" />
                        <label class="label">Password</label>
                        <input type="password" class="input" placeholder="Password" />
                        <div><a class="link link-hover">Forgot Password?</a></div>
                        <button class="btn btn-outline mt-4">Login</button>

                        <div class="divider">OR</div>

                        <button class="btn btn-outline btn-primary mt-2">Sign Up</button>

                        <a class="btn btn-secondary btn-outline mt-2" href="/demos/dashboard">See a Demo?</a>

                    </fieldset>
                </div>
            </div>
        </div>
    </div>
</div>